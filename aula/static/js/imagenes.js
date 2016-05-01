/**
 * Created by daniel on 30/04/16.
 */
function showImageList(){
    $('.toggle-class').fadeOut('fast', function (){
        $('#full-image-list').fadeIn('fast');
    });


}
function showUserImages(userId){
    $('.toggle-class').fadeOut('fast', function() {
        data = {name:'test'};
        $.get( "/imagenes/usuario/",data, function (data){
            console.log('Success');
            console.log(data);
        });
        $('#user-image-list').fadeIn('fast');
    });
    console.log('User: '+userId);
}

function addNewImage() {
    $('#add-new-image').slideDown(500);
}