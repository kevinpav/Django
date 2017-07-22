$(document).ready(function(){
    $('#ClickMe').click(function(){
        $.get("localhost:8000/message");
    });
});