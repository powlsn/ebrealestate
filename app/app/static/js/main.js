function ready(fn) {
    if(document.readyState === 'complete' || document.readyState === 'interactive') {
        setTimeout(fn, 1);
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}

ready(
    () => {
        const date = new Date();
        document.querySelector('.year').innerHTML = date.getFullYear();
    }
)