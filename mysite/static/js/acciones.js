var id = $('#id');
var nombre = $('#nombre');
var respuesta = $('#respuesta');
var tarea = $('#tarea');
var btn_tar = $('#btn-tar');
var btn_res = $('#btn-res');

id.hide();
nombre.hide();
respuesta.hide();


btn_res.on('click', function(){

	tarea.hide();
	respuesta.show();

});

btn_tar.on('click', function(){

	respuesta.hide();
	tarea.show();

});