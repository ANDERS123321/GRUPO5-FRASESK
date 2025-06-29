document.getElementById("getQuoteBtn").addEventListener("click", () => {
    fetch('/get-quote')
        .then(response => response.json())
        .then(data => {
            document.getElementById("quoteDisplay").innerText = data.quote;
            loadHistory();
        });
});

function loadHistory() {
    fetch('/history')
        .then(response => response.json())
        .then(data => {
            const historyList = document.getElementById("historyList");
            historyList.innerHTML = "";
            data.history.slice().reverse().forEach(quote => {
                const li = document.createElement("li");
                li.innerText = quote;
                historyList.appendChild(li);
            });
        });
}

window.onload = loadHistory;
