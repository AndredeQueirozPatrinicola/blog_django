// document.getElementById('editar-perfil').onclick = () => {
//     const documento = document.getElementById('div-perfil-meio');
//     documento.innerHTML = "Teste";

// }


if (!document.getElementById('login') && !document.getElementById('edit-perf')) 
{
    if (document.getElementsByTagName('label').length >= 4) 
    {
        const botoesImagem = document.getElementsByTagName('label')
        if (botoesImagem) 
        {
            let labelImagem = botoesImagem[3]
            labelImagem.classList.add('post-button')
        }

        const selectInput = document.getElementById('id_categoria')
        if (selectInput) 
        {
            selectInput.classList.add('select-input')
        }


    }
    else if (document.getElementsByTagName('label').length === 3) 
    {
        const botoesImagem = document.getElementsByTagName('label')

        if (botoesImagem) 
        {
            let labelImagem = botoesImagem[2]
            labelImagem.classList.add('post-button')
            labelImagem.style.width = '170px'
        }
    }
}else if(document.getElementById('id_password1'))
{
    const password_1 = document.getElementById('id_password1')
    const password_2 = document.getElementById('id_password2')

    password_1.classList.add('input-login')
    password_2.classList.add('input-login')
}


const sidebar = document.getElementById('sidebar-perfil') 
const editPerf = document.getElementById('edit-perf')
if (sidebar || editPerf)
{ 
    document.getElementById('base').style.marginTop = '5rem'
}


const helptext = document.getElementsByClassName('helptext')
if (helptext)
{
    helptext[0].style.display = 'none';
}

