// document.querySelector("label[for=firstName]").innerHTML = "Nombre";
// document.querySelector("label[for=lastName]").innerHTML = "Apellido";
// document.querySelector("label[for=username]").innerHTML = "Usuario";

const input = document.querySelector("#email");

input.addEventListener("invalid", (evento) => {
  let input = evento.target;
  let textHelp = input.nextElementSibling;
  textHelp.innerText = input.validationMessage;
});

input.addEventListener("input", (ev) => {
  let input = ev.target;
  input.classList.remove("is-valid", "is-invalid");
  if (input.checkValidity()) {
    input.classList.add("is-valid");
  } else {
    input.classList.add("is-invalid");
  }
});
