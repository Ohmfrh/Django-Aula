/**
 * Created by daniel on 30/04/16.
 */
function showImageList(){
    $('.toggle-class').fadeOut(250, function (){
        console.log(this);
        console.log('DONE');

    });

    setTimeout(function () {
        $('#full-image-list').fadeIn('fast');
    },250);
}

function showUserImages(userId){
    $('.toggle-class').fadeOut(250);
    setTimeout(function () {
        data = {userId: userId};
        $.get( "/imagenes/lista/",data, function (data){
            $('input:checkbox').removeAttr('checked');

            if (data.length != 0) {
                for (var i=0; i<data.length; i++) {
                    console.log(data[i]);
                    $('#id_Imagenes_'+data[i]['imageId']).prop('checked', true);
                }
            }

            $('#id_UserOwner').val(userId)
        });

        $('#user-image-list').fadeIn('fast');
    },250);


}

function addNewImage() {
    $('#add-new-image').slideDown(250);
}