// document.getElementById('editar-perfil').onclick = () => {
//     const documento = document.getElementById('div-perfil-meio');
//     documento.innerHTML = "Teste";
    
// }

if(document.getElementsByTagName('label').length >= 6)
{
    const botoesImagem = document.getElementsByTagName('label')
    if(botoesImagem)
    {
        let labelImagem = botoesImagem[3]
        labelImagem.classList.add('post-button')
    }

    const selectInput = document.getElementById('id_categoria')
    if(selectInput)
    {
        selectInput.classList.add('select-input')
    }
}
else if(document.getElementsByTagName('label').length === 3)
{
    const botoesImagem = document.getElementsByTagName('label')

    if(botoesImagem)
    {
        let labelImagem = botoesImagem[2]
        labelImagem.classList.add('post-button')
        labelImagem.style.width = '170px' 
    }
}


