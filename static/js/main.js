$(document).ready(function(){

  var markers = [];
  var mag = [];

  $("tbody tr").each(function(index, item){
    color($(item));
    markers.push({latLng: [$("td:eq(2)", item).text(), $("td:eq(3)", item).text()], name: index+" Mag: "+ $("td:eq(5)", item).text() +" at "+ $("td:eq(1)", item).text(), mag: $("td:eq(5)", item).text()});
  });

  markers.sort(function(a, b){
    return a.mag < b.mag ? 1
    : a.mag > b.mag ? -1
    : 0;
  });

  markers.forEach(function(el){
    mag.push(el.mag);
  });

  var map = new jvm.WorldMap({
    container: $('#world-map'),
    map: 'world_mill_en',
    markersSelectable: true,
    markers: markers,
    markerStyle: {
      initial: {
        fill: '#CA0020'
      }
    },
    series: {
      markers: [{
        attribute: 'r',
        scale: [2, 15],
        values: mag
      }]
    }
  });

  $("tbody tr button").click(function(e){
    map.clearSelectedMarkers();
    map.setSelectedMarkers([$(this).parents("tr").index()]);
   $('html, body').animate({
        scrollTop: $("#world-map").offset().top
    }, 500);
  });
});

function color($row){
  if($("td:eq(5)", $row).text() > 6.5){
    $row.addClass("danger");
  } else if($("td:eq(5)", $row).text() > 5){
    $row.addClass("warning");
  } else if($("td:eq(5)", $row).text() > 4.5){
    $row.addClass("success");
  }
}
