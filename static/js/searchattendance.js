const searchField = document.querySelector("#searchField");
searchField.addEventListener('keyup',(e)=>{
    const searchValue = e.target.value;

    if(searchValue.length>0){
        console.log("object",object);

        fetch("/search_attendance",{
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",
        })
        .then((res)=> res.json())
        .then((data) => {
            console.log("data", data);
        });

    }

});