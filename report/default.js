
//This is a canvas that will be copied into report.js for html document to find
const main = () => {
    console.log(data)
    data.forEach(session => {
        const container = document.getElementById("reports")
        container.innerHTML += `<p>${session.date}</p>`
    })
    
}

main()

