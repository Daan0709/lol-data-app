initiatePage();

async function initiatePage() {
    let champs = await fetch('http://localhost:5000/champions')
        .then(response => response.json())
        .then(data => {
            return data
        })

    let body = document.querySelector(".wrapper")
    champs.forEach((champ) => {
        let icon = document.createElement("img");
        icon.src = champ.icon;
        icon.classList += "icon";

        let title = document.createElement("div");
        body.append(title);
        title.append(icon);
        title.classList += "title-wrapper";
        title.innerHTML += `${champ.name},  ${champ.title}`;
        title.id = champ.id;
    })
}

async function filter() {
    let str = document.getElementById("searchbox").value;

    let champs = await fetch(`http://localhost:5000/champion/contains?substring=${str}`)
        .then(response => response.json())
        .then(data => {
            return data
        })

    let body = document.querySelector(".wrapper");
    body.innerHTML = ""
    champs.forEach((champ) => {
        let icon = document.createElement("img");
        icon.src = champ.icon;
        icon.classList += "icon";

        let title = document.createElement("div");
        body.append(title);
        title.append(icon);
        title.classList += "title-wrapper";
        title.innerHTML += `${champ.name},  ${champ.title}`;
        title.id = champ.id;
    })
}

async function redirectToChampPage(event) {
    let id = event.target.id;
    window.location.href = `http://localhost:5000/${id}`;
}