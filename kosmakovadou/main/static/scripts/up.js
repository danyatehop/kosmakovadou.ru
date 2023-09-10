document.addEventListener('scroll', up);

function up(){
    var upBtn = document.getElementById('up');
    if (window.scrollY > 400)
    upBtn.style.opacity = '100';
    else upBtn.style.opacity = '0';
}