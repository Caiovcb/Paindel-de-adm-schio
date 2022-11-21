const btn = document.querySelector("button");
const divMessage = document.querySelector(".success");

const msg = "Tipo Registrado!";

function ativar(msg) {
    const message = document.createElement("div");
    message.classList.add("message");
    message.innerText = msg;
    divMessage.appendChild(message);
}



btn.addEventListener("click", () => {
    ativar(msg);
});