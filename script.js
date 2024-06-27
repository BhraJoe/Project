let just  = document.getElementById("just")
let popular  = document.getElementById("popular")
let tv  = document.getElementById("tv")
let free  = document.getElementById("free")

document.getElementById("just_tab").style.display = "block";
document.getElementById("popular_tab").style.display = "none";
document.getElementById("tv_tab").style.display = "none";
document.getElementById("free_tab").style.display = "none";

just.onclick = ()=> {
    document.getElementById("just_tab").style.display = "block";
    document.getElementById("popular_tab").style.display = "none";
    document.getElementById("tv_tab").style.display = "none";
    document.getElementById("free_tab").style.display = "none"; 
}

popular.onclick = ()=> {
    document.getElementById("just_tab").style.display = "block";
    document.getElementById("popular_tab").style.display = "block";
    document.getElementById("tv_tab").style.display = "none";
    document.getElementById("free_tab").style.display = "none"; 
}

tv.onclick = ()=> {
    document.getElementById("just_tab").style.display = "none";
    document.getElementById("popular_tab").style.display = "none";
    document.getElementById("tv_tab").style.display = "block";
    document.getElementById("free_tab").style.display = "none"; 
}

free.onclick = ()=> {
    document.getElementById("just_tab").style.display = "none";
    document.getElementById("popular_tab").style.display = "none";
    document.getElementById("tv_tab").style.display = "none";
    document.getElementById("free_tab").style.display = "block"; 
}