import math, json, sys

def plural(n, one, many):
    return one if n == 1 else many

def a_an(n):
    s = str(n)
    return "An" if (n == 11 or n == 18 or s.startswith("8")) else "A"

def pass_count(claim, need):
    if not (claim > 0):
        raise ValueError("the claimed inches must be above zero")
    if not (need > 0):
        raise ValueError("the depth must be above zero")
    return math.ceil(need / claim)

def depth_truth(claim, need):
    passes = pass_count(claim, need)
    if passes <= 1:
        verdict = "one honest pass"
    elif passes <= 3:
        verdict = "a few honest passes"
    elif passes <= 6:
        verdict = "a patient rhythm"
    else:
        verdict = "a ladder of passes, honestly"
    return f"The grinder claims {claim} {plural(claim, 'inch', 'inches')} a pass; {need} {plural(need, 'inch', 'inches')} below grade is {passes} {plural(passes, 'pass', 'passes')} - {verdict}."

def chips_cubic_feet(diameter, depth):
    if not (diameter > 0):
        raise ValueError("the stump diameter must be above zero")
    if not (depth > 0):
        raise ValueError("the depth must be above zero")
    return math.pi * (diameter / 2) * (diameter / 2) * depth / 1728

def mulch_truth(diameter, depth, bag_size):
    if not (bag_size > 0):
        raise ValueError("the bag size must be above zero")
    chips = chips_cubic_feet(diameter, depth)
    bags = math.ceil(chips / bag_size)
    if bags <= 1:
        verdict = "one bag at the beds"
    elif bags <= 3:
        verdict = "a few trips to the beds"
    elif bags <= 8:
        verdict = "a wheelbarrow of trips"
    else:
        verdict = "the beds will not take it all"
    return f"{a_an(diameter)} {diameter}-inch stump ground {depth} {plural(depth, 'inch', 'inches')} deep makes about {chips:.1f} cubic feet of chips - about {bags} {plural(bags, 'bag', 'bags')} of {bag_size} cubic {plural(bag_size, 'foot', 'feet')} each, {verdict}."

def afternoon_truth(stumps, minutes):
    if not (stumps > 0):
        raise ValueError("the stump count must be above zero")
    if not (minutes > 0):
        raise ValueError("the minutes must be above zero")
    total = stumps * minutes
    if total <= 45:
        verdict = "done before lunch"
    elif total <= 120:
        verdict = "a working morning"
    elif total <= 300:
        verdict = "an honest afternoon"
    else:
        verdict = "a two-day rental, honestly"
    return f"{stumps} {plural(stumps, 'stump', 'stumps')} at {minutes} {plural(minutes, 'minute', 'minutes')} each is {total:.1f} minutes of grinding - {verdict}."

FNS = {
    "depthTruth": depth_truth,
    "mulchTruth": mulch_truth,
    "afternoonTruth": afternoon_truth,
}

cases = [
 {
  "fn": "depthTruth",
  "args": [
   4,
   12
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   4,
   13
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   6,
   6
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   3,
   2
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   2,
   15
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   1,
   10
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   5,
   20
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   0,
   12
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   4,
   0
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   24,
   8,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   12,
   6,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   36,
   10,
   3
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   18,
   8,
   1
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   8,
   4,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   48,
   12,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   30,
   9,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   0,
   8,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   24,
   0,
   2
  ]
 },
 {
  "fn": "mulchTruth",
  "args": [
   24,
   8,
   0
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   3,
   25
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   1,
   30
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   6,
   20
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   10,
   35
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   12,
   45
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   2,
   15
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   0,
   25
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   3,
   0
  ]
 },
 {
  "fn": "depthTruth",
  "args": [
   5,
   1
  ]
 },
 {
  "fn": "afternoonTruth",
  "args": [
   4,
   1
  ]
 }
]
out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
