document.addEventListener('DOMContentLoaded', function () {
    const menuLinks = document.querySelectorAll('.menu-a');
    const detailItems = document.querySelectorAll('.detail-item');

    menuLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const category = this.textContent;
            updateProductList(category);
        });
    });

    function updateProductList(category) {
        detailItems.forEach(item => {
            const itemCategory = item.dataset.category;
            if (category === 'Все товары' || itemCategory === category) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
        // Обновляем заголовок категории
        const titleCategory = document.querySelector('.title-category');
        titleCategory.textContent = category;
    }
});
