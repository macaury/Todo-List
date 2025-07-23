// Modal para confirmar a exclusão da tarefa

document.querySelectorAll(".delete-btn").forEach(
    btn => {
        btn.addEventListener("click",function(e){
            e.preventDefault();
            
            const delLink = this.getAttribute("href");

            if (delLink && confirm("Quer deletar esta Tarefa?"))
                {
                window.location.href=delLink;
            }
        });
    }
);



// função de pesquisa

document.getElementById("search-btn").addEventListener("click",function(){
    document.getElementById("search-form").onsubmit();
});



