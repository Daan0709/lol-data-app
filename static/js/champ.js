initiatePage()
let champ;

async function initiatePage(){
    let url = document.URL.split("/");
    let id = url[url.length -1];
    console.log(id);

    this.champ = await fetch(`http://localhost:5000/championid?id=${id}`)
        .then(response => response.json())
        .then(data => {
            return data
        })

    document.querySelector("body").innerHTML = this.champ.name + ", " + this.champ.title;
    console.log(this.champ);
}