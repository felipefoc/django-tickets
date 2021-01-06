function fireSweet(){
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'Nova ticket cadastrado',
      text: 'Agora é só aguardar a solução',
      showConfirmButton: false,
      timer: 3000
    })
  }

$(document).ready(function(){
  let form = $('#buttonform');
    form.on("click",function(){       
        if ( validate() === true ){
            fireSweet();
            setTimeout( function () { 
                $('form').submit();
              }, 3000 );
        } else {
            Swal.fire({
                position: 'center',
                icon: 'error',
                title: 'Campos em branco, favor preencher.',
                showConfirmButton: false,
                timer: 1500
                })
                };
            })
        })

  function validate() {
      let tipo = $('#id_tipo')
      let setor = $('#id_setor')
      let desc = $('#id_descrição')
      
      if (tipo.val() == '' || setor.val() == '' || desc.val() == '') {
          return false;
      }
      else {
          return true;
      }
  }
    
