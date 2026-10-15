// Stump Math engine - hypothetical arithmetic with labeled norms only.
// No verdicts about what any machine can safely grind: that is the manufacturer's call.

function plural(n, one, many) { return n === 1 ? one : many; }

function aAn(n) {
  const s = String(n);
  return (n === 11 || n === 18 || s.startsWith("8")) ? "An" : "A";
}

function passCount(claim, need) {
  if (!(claim > 0)) throw new Error("the claimed inches must be above zero");
  if (!(need > 0)) throw new Error("the depth must be above zero");
  return Math.ceil(need / claim);
}

function depthTruth(claim, need) {
  const passes = passCount(claim, need);
  let verdict;
  if (passes <= 1) verdict = "one honest pass";
  else if (passes <= 3) verdict = "a few honest passes";
  else if (passes <= 6) verdict = "a patient rhythm";
  else verdict = "a ladder of passes, honestly";
  return `The grinder claims ${claim} ${plural(claim, "inch", "inches")} a pass; ${need} ${plural(need, "inch", "inches")} below grade is ${passes} ${plural(passes, "pass", "passes")} - ${verdict}.`;
}

function chipsCubicFeet(diameter, depth) {
  if (!(diameter > 0)) throw new Error("the stump diameter must be above zero");
  if (!(depth > 0)) throw new Error("the depth must be above zero");
  return Math.PI * (diameter / 2) * (diameter / 2) * depth / 1728;
}

function mulchTruth(diameter, depth, bagSize) {
  if (!(bagSize > 0)) throw new Error("the bag size must be above zero");
  const chips = chipsCubicFeet(diameter, depth);
  const bags = Math.ceil(chips / bagSize);
  let verdict;
  if (bags <= 1) verdict = "one bag at the beds";
  else if (bags <= 3) verdict = "a few trips to the beds";
  else if (bags <= 8) verdict = "a wheelbarrow of trips";
  else verdict = "the beds will not take it all";
  return `${aAn(diameter)} ${diameter}-inch stump ground ${depth} ${plural(depth, "inch", "inches")} deep makes about ${chips.toFixed(1)} cubic feet of chips - about ${bags} ${plural(bags, "bag", "bags")} of ${bagSize} cubic ${plural(bagSize, "foot", "feet")} each, ${verdict}.`;
}

function afternoonTruth(stumps, minutes) {
  if (!(stumps > 0)) throw new Error("the stump count must be above zero");
  if (!(minutes > 0)) throw new Error("the minutes must be above zero");
  const total = stumps * minutes;
  let verdict;
  if (total <= 45) verdict = "done before lunch";
  else if (total <= 120) verdict = "a working morning";
  else if (total <= 300) verdict = "an honest afternoon";
  else verdict = "a two-day rental, honestly";
  return `${stumps} ${plural(stumps, "stump", "stumps")} at ${minutes} ${plural(minutes, "minute", "minutes")} each is ${total.toFixed(1)} minutes of grinding - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { passCount, depthTruth, chipsCubicFeet, mulchTruth, afternoonTruth };
    }
