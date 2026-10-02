let nome = 'Patrick Franco';
console.log(nome);

function alerta(){
    alert("Você precisa clicar para enviar, tente novamente!")
}

function input(){
    let campo = document.querySelector('input');
    if(campo.value.length >= 3){
        campo.value = '';
    }
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    }
}, true);