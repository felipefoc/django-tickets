function validate() {
    let pass1 = $('#id_new_password1')
    let pass2 = $('#id_new_password2')
      
    if ( pass1.val() === '' || pass2.val() === '' ) {
        erro = 'Campo em branco';
        return false;
    } else if ( pass1.val().length > 8 && pass1.val() != pass2.val() ) {
        erro = 'Senhas não conferem';
        return false;
    } else if ( pass1.val() !== pass2.val() ) {
        erro = 'Senhas não conferem';
        return false;
    } else {
        return true;
    }
}

function fireSweet(){
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'Senha atualizada',
      showConfirmButton: false,
      timer: 3000
    })
  }

$(document).ready(function(){
  let form = $('#buttonform');
    form.on("click",function(){
        if ( validate() == true ){
            fireSweet();
            setTimeout( function () { 
                $('#formm').submit();
              }, 3000 );
        } else {
            Swal.fire({
                position: 'center',
                icon: 'error',
                title: erro,
                showConfirmButton: false,
                timer: 3000
                })
                };
            })
        })


