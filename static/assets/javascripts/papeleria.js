$('#id_estado').change(function(){
    $.ajax({
        data : {'id':$('#id_estado').val()},
		url : '/usuarios/carga_mun',
		type : 'GET',
		success: function(data){
            $('#id_municipio').children().remove();
			for (i=0;i<data.length;i++)
            {
                $("#id_municipio").append('<option value='+data[i]['id']+'>'+data[i]['municipio']+'</option>');

            }
		},
		error : function(xhr,errmsg,err) {
	        console.log(xhr.responseText);
	    }
    });
});


function eliminarPost(id) {
    var form = document.formulario;
    form.id_articulo.value=id;
    form.submit();

}