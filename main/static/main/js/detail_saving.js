const logRows = document.querySelectorAll('.log-row')

const modal = document.querySelector('.modal') 
const modalsClose = document.querySelectorAll('.modal-close')
const modalFields = document.querySelectorAll('.modal-body div .modal-field')
const modalDetail = document.querySelector('.modal-detail')

const modalDelete = document.querySelector('.modal-delete')
const btnDeleteConfirm = document.querySelector('.btn-delete-confirm')
const modalBtnDelete = document.querySelector('.modal-btn-delete')

modalsClose.forEach(modalClose => {
    modalClose.addEventListener('click', e => {
        modal.classList.replace('flex', 'hidden')
    })
})

logRows.forEach(row => {
    row.addEventListener('click', function () {
        modalDetail.classList.replace('hidden', 'inline')
        modal.classList.replace('hidden', 'flex')
    
        modalDelete.classList.replace('inline', 'hidden')
        modalBtnDelete.classList.replace('inline', 'hidden')

        const data = [...this.querySelectorAll('td')].map(content => content.textContent)

        modalFields.forEach((field, i) => {
            if (data[2] === 'Keluar') {
                modalFields[2].classList.replace('text-green-600','text-red-600')
            } else if (data[2] === 'Masuk') {
                modalFields[2].classList.replace('text-red-600', 'text-green-600')
            }
            field.textContent = data[i]
            
        })
    })
})

btnDeleteConfirm.addEventListener('click', () => {    
    modalDetail.classList.replace('inline', 'hidden')

    modalDelete.classList.replace('hidden', 'inline')
    modalBtnDelete.classList.replace('hidden', 'inline')

    modal.classList.replace('hidden', 'flex')
})

const navbar = document.querySelector('nav')
window.addEventListener('scroll', (e) => {
    if (window.scrollY > 25) {
        navbar.classList.add('bg-primary')
        navbar.classList.add('shadow-md')
    } else {
        navbar.classList.remove('bg-primary')
        navbar.classList.remove('shadow-md')
    }
})

const nominals = document.querySelectorAll('.nominal')
nominals.forEach(nominal => {
    const convertToCurrencyFormate = parseFloat(nominal.textContent).toLocaleString(locale = 'id')
    nominal.textContent = convertToCurrencyFormate
    
})

