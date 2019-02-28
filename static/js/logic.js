function buildMetadata(channel) {

    // @TODO: Complete the following function that builds the metadata panel
    var meta = `/metadata/${channel}`;
    // Use `d3.json` to fetch the metadata for a sample
    d3.json(meta).then(function (channel) {
        var channel_metadata = d3.select("#channel-metadata");

        // Use d3 to select the panel with id of `#sample-metadata`

        // Use `.html("") to clear any existing metadata
        channel_metadata.html("");
        console.log(channel);
        // Use `Object.entries` to add each key and value pair to the panel
        // Hint: Inside the loop, you will need to use d3 to append new
        // tags for each key-value in the metadata.
        Object.entries(channel).forEach(function ([key, value]) {
            var row = channel_metadata.append("p");
            row.text(`${key}: ${value}`);
        });
        // BONUS: Build the Gauge Chart
        // buildGauge(data.WFREQ);
    });
}

function init() {
    // Grab a reference to the dropdown select element
    var input = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/name").then((channelName) => {
      channelNames.forEach((channel) => {
        input
          .append("option")
          .text(channelName)
          .property("value", channel);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = sampleNames[0];
    //   buildCharts(firstChannel);
      buildMetadata(firstChannel);
    });
  }
  
  function optionChanged(newChannel) {
    // Fetch new data each time a new sample is selected
    // buildCharts(newChannel);
    buildMetadata(newChannel);
  }
  
  // Initialize the dashboard
  init();
  