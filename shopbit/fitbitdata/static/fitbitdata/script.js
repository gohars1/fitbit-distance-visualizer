$(document).ready(function(){
    $(".sharebutton").click(function(){
        const csrftoken = Cookies.get('csrftoken');
        var badge = $(this).attr("value");
        var json = { "badgename" : badge }

        $.ajax({
            type: 'POST',
            url: '/share/',
            headers: { 'X-CSRFToken': csrftoken },
            data: json,
            success: function(){
                console.log("great!")
            },
            error: function(){
                console.log("wrang");
            }
        })
    }); 
});
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');