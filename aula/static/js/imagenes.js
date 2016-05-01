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
    $('.toggle-class').fadeOut(250, function() {
        data = {name:'test'};
        $.get( "/imagenes/lista/",data, function (data){
            console.log('Success');
            console.log(data);
        });
    });

    setTimeout(function () {
        $('#user-image-list').fadeIn('fast');
    },250);

    console.log('User: '+userId);
}

function addNewImage() {
    $('#add-new-image').slideDown(250);
}