from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AutenticacionTests(TestCase):

    def test_registro_crea_usuario_y_redirige_al_login(self):
        respuesta = self.client.post(
            reverse("registrar"),
            {
                "username": "nuevo",
                "email": "nuevo@example.com",
                "password1": "clave-segura-123",
                "password2": "clave-segura-123",
            },
        )
        self.assertRedirects(respuesta, reverse("iniciar_sesion"))
        self.assertTrue(User.objects.filter(username="nuevo").exists())

    def test_login_y_logout(self):
        User.objects.create_user("tomas", password="clave-segura-123")

        respuesta = self.client.post(
            reverse("iniciar_sesion"), {"username": "tomas", "password": "clave-segura-123"}
        )
        self.assertRedirects(respuesta, reverse("inicio"))
        self.assertIn("_auth_user_id", self.client.session)

        respuesta = self.client.post(reverse("cerrar_sesion"))
        self.assertRedirects(respuesta, reverse("inicio"))
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_login_con_credenciales_incorrectas(self):
        User.objects.create_user("tomas", password="clave-segura-123")
        respuesta = self.client.post(
            reverse("iniciar_sesion"), {"username": "tomas", "password": "incorrecta"}
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)
