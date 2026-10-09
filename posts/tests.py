import shutil
import tempfile
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from posts.models import Posteo

MEDIA_TEMPORAL = tempfile.mkdtemp()


def imagen_de_prueba(nombre="foto.png"):
    buffer = BytesIO()
    Image.new("RGB", (20, 20), "teal").save(buffer, format="PNG")
    return SimpleUploadedFile(nombre, buffer.getvalue(), content_type="image/png")


@override_settings(MEDIA_ROOT=MEDIA_TEMPORAL)
class PosteoTests(TestCase):

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA_TEMPORAL, ignore_errors=True)

    def setUp(self):
        self.usuario = User.objects.create_user("tomas", password="clave-segura-123")
        self.posteo = Posteo.objects.create(
            titulo="Post de prueba", autor="Tomás", contenido="Contenido", imagen=imagen_de_prueba()
        )

    def test_listado_y_detalle_son_publicos(self):
        self.assertEqual(self.client.get(reverse("lista_posts")).status_code, 200)
        respuesta = self.client.get(reverse("detalle_post", args=[self.posteo.pk]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, self.posteo.imagen.url)

    def test_rutas_protegidas_redirigen_al_login(self):
        rutas = [
            reverse("crear_post"),
            reverse("editar_post", args=[self.posteo.pk]),
            reverse("borrar_post", args=[self.posteo.pk]),
            reverse("perfil"),
            reverse("editar_perfil"),
        ]
        for ruta in rutas:
            with self.subTest(ruta=ruta):
                respuesta = self.client.get(ruta)
                self.assertRedirects(respuesta, f"{reverse('iniciar_sesion')}?next={ruta}")

    def test_crear_post_con_imagen(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("crear_post"),
            {"titulo": "Nuevo", "autor": "Tomás", "contenido": "Texto", "imagen": imagen_de_prueba("nuevo.png")},
        )
        self.assertRedirects(respuesta, reverse("lista_posts"))
        nuevo = Posteo.objects.get(titulo="Nuevo")
        self.assertTrue(nuevo.imagen.name.startswith("posteo/"))

    def test_editar_post(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("editar_post", args=[self.posteo.pk]),
            {"titulo": "Editado", "autor": "Tomás", "contenido": "Otro texto"},
        )
        self.assertRedirects(respuesta, reverse("lista_posts"))
        self.posteo.refresh_from_db()
        self.assertEqual(self.posteo.titulo, "Editado")

    def test_borrar_post(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(reverse("borrar_post", args=[self.posteo.pk]))
        self.assertRedirects(respuesta, reverse("lista_posts"))
        self.assertFalse(Posteo.objects.filter(pk=self.posteo.pk).exists())
