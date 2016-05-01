/**
 * Created by daniel on 1/05/16.
 */
function showSongList(){
    $('.toggle-class').fadeOut(250, function (){
        console.log(this);
        console.log('DONE');

    });

    setTimeout(function () {
        $('#full-song-list').fadeIn('fast');
    },250);
}

function showUserSongs(userId){
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

        $('#user-song-list').fadeIn('fast');
    },250);


}

function addNewSong() {
    $('#add-new-song').slideDown(250);
}