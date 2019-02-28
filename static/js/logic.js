function buildMetadata(sample) {

    // @TODO: Complete the following function that builds the metadata panel
    var meta = `/metadata/${sample}`;
    // Use `d3.json` to fetch the metadata for a sample
    d3.json(meta).then(function (sample) {
        var sample_metadata = d3.select("#sample-metadata");

        // Use d3 to select the panel with id of `#sample-metadata`

        // Use `.html("") to clear any existing metadata
        sample_metadata.html("");
        console.log(sample);
        // Use `Object.entries` to add each key and value pair to the panel
        // Hint: Inside the loop, you will need to use d3 to append new
        // tags for each key-value in the metadata.
        Object.entries(sample).forEach(function ([key, value]) {
            var row = sample_metadata.append("p");
            row.text(`${key}: ${value}`);
        });
        // BONUS: Build the Gauge Chart
        // buildGauge(data.WFREQ);
    });
}