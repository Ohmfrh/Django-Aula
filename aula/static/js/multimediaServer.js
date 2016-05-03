/**
 * Created by daniel on 1/05/16.
 */
function addServer() {
    console.log('Add Server');
}

function editServer(serverId) {
    console.log(serverId);
    console.log('Edit Server');
    $('#id_dirEdit').val('');
    $('#id_usrEdit').val('');
    $('#id_passEdit').val('');
    $('#id_serverId').val(serverId);

    data = {serverId: serverId};

    $.get( "/multimedia/servidor/",data, function (data){
        data = JSON.parse(data);
        $('#id_dirEdit').val(data['address']);
        $('#id_usrEdit').val(data['user']);
        $('#id_passEdit').val(data['password']);
        $('#delete-server').attr('name', serverId)
    });
}

function deleteServer(serverId) {
    console.log('Delete: ' + serverId)
}