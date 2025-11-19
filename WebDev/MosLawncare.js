// Desc: Mo's Lawncare Services
// Author: Megan Hickey
// Dates: November 13, 2025

var $ = function (id) {
  return document.getElementById(id);
};

// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Define program constants.

const BORDER_SIZE = 0.04; // Borders are 4% of total sq ftg
const BORDER_RATE = 0.28; // Borders are charged at 28 cents per sq ft
const LAWN_SIZE = 0.95; // Mowing is based on the remaining 95%
const LAWN_MOW_RATE = 0.04; // 4 cents per sq ft
const FERT_RATE = 0.03; // Charged at 3 cents per sq ft
const HST_RATE = 0.15; // Hst is 15% of the total charges
const ENV_RATE = 0.014; // Environmental tax is 1.4% of the total charges

// Start main program here.

// Gather customer inputs.

let CustName = prompt("Enter the customer name:   ");
let CustSt = prompt("Enter the street address:    ");
let City = prompt("Enter the city:           ");
let PhoneNum = prompt("Enter the phone number (999-999-9999):     ");

let TotSqFt = parseInt(
  prompt("Enter the total square feet of the property (#####):     ")
);

// Perform program calculations.

let BorderSqFt = TotSqFt * BORDER_SIZE;
let BorderTrimCost = BorderSqFt * BORDER_RATE;

let LawnSqFt = TotSqFt - BorderSqFt;
let LawnMowCost = LawnSqFt * LAWN_MOW_RATE;

let FertTreatCost = TotSqFt * FERT_RATE;

let TotalCharge = BorderTrimCost + LawnMowCost + FertTreatCost;

let HstCost = TotalCharge * HST_RATE;
let EnvTax = TotalCharge * ENV_RATE;

let InvoiceTotal = TotalCharge + HstCost + EnvTax;

// Generate program results

document.writeln("<br/>");
document.writeln("<table class='servicetable'>");

document.writeln("<tr class='orangeback'>");
document.writeln(
  "<td colspan='2'><br/>Mo's Lawncare Services - Customer Invoice<br/><br/></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'><br/>Customer details:<br/><br/>" +
    "&nbsp " +
    CustName +
    "<br/>" +
    "&nbsp " +
    CustSt +
    "<br/>" +
    "&nbsp " +
    City +
    "&nbsp " +
    PhoneNum +
    "<br/>" +
    "<br/>" +
    "Property size (in sq ft):" +
    " " +
    TotSqFt +
    "<br/>" +
    "<br/>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='lefttext'>Border cost: </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(BorderTrimCost) + "</td>"
);

document.writeln("</tr>");
document.writeln("<tr>");
document.writeln("<td class='lefttext'>Mowing cost: </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(LawnMowCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='lefttext'>Fertilizer cost: </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(FertTreatCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br/></td>");
document.writeln("<td><br/></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='lefttext'>Total charges: </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(TotalCharge) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br/></td>");
document.writeln("<td><br/></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='lefttext'>Sales tax (HST): </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(HstCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='lefttext'>Environmental tax: </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(EnvTax) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br/></td>");
document.writeln("<td><br/></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='lefttext'>Invoice Total: </td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(InvoiceTotal) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr class='orangeback'>");
document.writeln(
  "<td colspan='2' class='centertext'><br/>Turning Lawns into Landscapes<br/><br/></td>"
);
document.writeln("</tr>");

document.writeln("</table>");
document.writeln("<br/>");
