const savings_title = document.querySelectorAll('.saving_title')
savings_title.forEach(item => {
    if (item.textContent.length > 15 ) {
        item.classList.replace('md:text-5xl', 'md:text-4xl')
    }
})

const nominal = document.querySelectorAll('.nominal')
nominal.forEach(e => {
    const convertToLocale = parseFloat(e.textContent).toLocaleString('id')
    e.textContent = convertToLocale
})

const alerts = document.querySelectorAll('.alert')
alerts.forEach(alert => {
    const close = alert.querySelector('.close')
    close.addEventListener('click', () => alert.remove())
})