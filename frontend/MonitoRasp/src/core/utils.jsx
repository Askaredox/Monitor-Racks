export const emailValidator = (email) => {
  const re = /\S+@\S+\.\S+/;

  if (!email || email.length <= 0) return "Email no puede estar vacío.";
  if (!re.test(email)) return "Se necesita un correo válido.";

  return "";
};

export const passwordValidator = (password) => {
  if (!password || password.length <= 0) return "Contraseña no puede estar vacía.";

  return "";
};

export const nameValidator = (name) => {
  if (!name || name.length <= 0) return "Name cannot be empty.";

  return "";
};
