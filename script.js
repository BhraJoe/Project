let just  = document.getElementById("just_tab")
let popular  = document.getElementById("popular_tab")
let tv  = document.getElementById("tv_tab")
let free  = document.getElementById("free_tab")

document.getElementById("just").style.display = "block";
document.getElementById("popular").style.display = "none";
document.getElementById("tv").style.display = "none";
document.getElementById("free").style.display = "none";

just.onclick = ()=> {
    document.getElementById("just").style.display = "block";
    document.getElementById("popular").style.display = "none";
    document.getElementById("tv").style.display = "none";
    document.getElementById("free").style.display = "none"; 
    just.style.borderBottom = "1px solid red"
    popular.style.borderBottom = "white"
    tv.style.borderBottom = "white"
    free.style.borderBottom = "white"
}

popular.onclick = ()=> {
    document.getElementById("just").style.display = "none";
    document.getElementById("popular").style.display = "block";
    document.getElementById("tv").style.display = "none";
    document.getElementById("free").style.display = "none"; 
    just.style.borderBottom = "white"
    popular.style.borderBottom = "1px solid red"
    tv.style.borderBottom = "white"
    free.style.borderBottom = "white"
}

tv.onclick = ()=> {
    document.getElementById("just").style.display = "none";
    document.getElementById("popular").style.display = "none";
    document.getElementById("tv").style.display = "block";
    document.getElementById("free").style.display = "none"; 
    just.style.borderBottom = "white"
    popular.style.borderBottom = "white"
    tv.style.borderBottom = "1px solid red"
    free.style.borderBottom = "white"
}

free.onclick = ()=> {
    document.getElementById("just").style.display = "none";
    document.getElementById("popular").style.display = "none";
    document.getElementById("tv").style.display = "none";
    document.getElementById("free").style.display = "block"; 
    just.style.borderBottom = "white"
    popular.style.borderBottom = "white"
    tv.style.borderBottom = "white"
    free.style.borderBottom = "1px solid red"
}