$(document).ready(function(){
    var value = $('#theme').val();
    document.documentElement.style.setProperty('--changer',value)

    var value2 = $('#theme2').val();
    document.documentElement.style.setProperty('--changer2',value2)
})

