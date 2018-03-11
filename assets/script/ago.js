function ago(date) {
    function render(n, unit) {
        return n + " " + unit + ((n == 1) ? "" : "s") + " ago";
    }

    var seconds = Math.floor((new Date() - date) / 1000);

    var interval = Math.floor(seconds / (60 * 60 * 24 * 30 * 365));
    if (Math.floor(seconds / (60 * 60 * 24 * 30 * 365)) >= 1) {
        return render(interval, "year");
    }
    interval = Math.floor(seconds / (60 * 60 * 24 * 30));
    if (interval >= 1) {
        return render(interval, "month");
    }
    interval = Math.floor(seconds / (60 * 60 * 24));
    if (interval >= 1) {
        return render(interval, "day");
    }
    interval = Math.floor(seconds / (60 * 60));
    if (interval >= 1) {
        return render(interval, "hour");
    }
    interval = Math.floor(seconds / 60);
    if (interval >= 1) {
        return render(interval, "minute");
    }
    interval = Math.floor(seconds);
    return render(interval, "second");
}

var date = Date.parse(document.getElementById("postedon").getAttribute("datetime"));
document.getElementById("postedago").innerHTML = ago(date);
