$(document).ready(function(){
    $('.menu-a').click(function(event){
        event.preventDefault(); // Предотвращаем перезагрузку страницы
        var category = $(this).text();
        $.ajax({
            url: '/products/' + category + '/',
            method: 'GET',
            success: function(data) {
                $('.main-details').html(data);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
