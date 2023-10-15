$(document).ready(function () {
    new DataTable("#example");
    new DataTable("#scroll-vertical", {
        scrollY: "210px",
        scrollCollapse: true,
        paging: false,
    });
    new DataTable("#scroll-horizontal", { scrollX: true });
    new DataTable("#alternative-pagination", { pagingType: "full_numbers" });

    var e = $("#add-rows").DataTable();
    var a = 1;

    $("#addRow").on("click", function () {
        e.row
            .add([
                a + ".1",
                a + ".2",
                a + ".3",
                a + ".4",
                a + ".5",
                a + ".6",
                a + ".7",
                a + ".8",
                a + ".9",
                a + ".10",
                a + ".11",
                a + ".12",
            ])
            .draw(false);
        a++;
    });
    $("#addRow").click();

    $("#example").DataTable();

    new DataTable("#fixed-header", { fixedHeader: true });

    new DataTable("#model-datatables", {
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal({
                    header: function (e) {
                        e = e.data();
                        return "Details for " + e[0] + " " + e[1];
                    },
                }),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll({
                    tableClass: "table",
                }),
            },
        },
    });

    new DataTable("#buttons-datatables", {
        dom: "Bfrtip",
        buttons: ["copy", "csv", "excel", "print", "pdf"],
    });

    new DataTable("#ajax-datatables", { ajax: "assets/json/datatable.json" });
});
