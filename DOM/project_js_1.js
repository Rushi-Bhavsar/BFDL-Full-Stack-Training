var all_columns = document.querySelectorAll("td")

function changeMarker(){
    if (this.textContent === '')
        this.textContent = 'X'
    else if (this.textContent === 'X')
        this.textContent = 'O'
    else
        this.textContent = ''
}

for (column of all_columns){
    column.addEventListener('click', changeMarker)
}