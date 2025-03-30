
//alert("teste") 


function delete_conceito(designation){
    $.ajax("/conceitos/"+ designation, {
        type: "DELETE",
        success: function(data) {
            console.log(data)
            if (data["success"]){
                window.location.href = data["redirect_url"]
            } 
        },
        error: function(error){
            console.log(error)
        }
    })
    // o $ é o jquery
}
    
// para as tabelas funcionarem
// é executado quando a página é carregada
$(document).ready( function () {
    $('#tabela_conceitos').DataTable({
        "search": {
            "regex": true  // pesquisa com expressões regulares
        }
    });
} );

