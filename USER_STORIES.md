# Café Calle Ocho — User Story Backlog

**Course:** EGN 475 · Week 2 · Assignment 2.1  
**Student:** Roy Diaz  
**Project:** Option A — Café Calle Ocho pickup ordering prototype

Priorities: **Must** = essential prototype, **Should** = valuable later, **Could** = optional. These stories are proposed for the prototype and will be reviewed against INVEST with GitHub Copilot.

## US-01 — Customer — Must

As a customer, I want to browse the café menu so that I can choose what to order.

**Acceptance criterion 1 — normal case**
- **Given** the café has available menu items,
- **When** I open the menu,
- **Then** I see each available item's name, description, and price.

**Acceptance criterion 2 — edge case**
- **Given** the café has no menu items available,
- **When** I open the menu,
- **Then** I see a clear message that no items are currently available.

## US-02 — Customer — Must

As a customer, I want to select items and quantities so that I can prepare a pickup order.

**Acceptance criterion 1 — normal case**
- **Given** an available item is displayed,
- **When** I choose a quantity of two,
- **Then** my order selection shows two of that item.

**Acceptance criterion 2 — edge case**
- **Given** I am selecting an item,
- **When** I enter a quantity of zero or less,
- **Then** the system rejects the quantity and asks for at least one.

## US-03 — Customer — Must

As a customer, I want to submit my pickup order so that the kitchen can prepare it.

**Acceptance criterion 1 — normal case**
- **Given** my order contains at least one available item,
- **When** I submit it,
- **Then** the system records the order with the status received.

**Acceptance criterion 2 — edge case**
- **Given** my order has no items,
- **When** I attempt to submit it,
- **Then** the system prevents submission and explains that I must select an item.

## US-04 — Customer — Must

As a customer, I want an order confirmation number so that I can identify my pickup order.

**Acceptance criterion 1 — normal case**
- **Given** my order has been accepted,
- **When** the confirmation appears,
- **Then** I see an order number and a summary of my items.

**Acceptance criterion 2 — edge case**
- **Given** my order submission fails,
- **When** the system cannot create the order,
- **Then** no confirmation number is shown and I see an error message.

## US-05 — Customer — Must

As a customer, I want to check my order status so that I know when it is ready for pickup.

**Acceptance criterion 1 — normal case**
- **Given** I have a valid order number,
- **When** I check its status,
- **Then** I see its current status as received, preparing, ready, or picked up.

**Acceptance criterion 2 — edge case**
- **Given** I enter an order number that does not exist,
- **When** I check its status,
- **Then** I see an order-not-found message without another customer's information.

## US-06 — Kitchen staff — Must

As a kitchen staff member, I want to see incoming orders so that I know what to prepare next.

**Acceptance criterion 1 — normal case**
- **Given** new orders have been received,
- **When** I open the kitchen board as staff,
- **Then** I see their order numbers, items, and current statuses.

**Acceptance criterion 2 — edge case**
- **Given** I am not authorized as kitchen staff,
- **When** I try to open the kitchen board,
- **Then** access is denied.

## US-07 — Kitchen staff — Must

As a kitchen staff member, I want to advance an order's status so that customers can follow its progress.

**Acceptance criterion 1 — normal case**
- **Given** an order is received and I am authorized staff,
- **When** I select Start preparing,
- **Then** its status changes to preparing on the kitchen board.

**Acceptance criterion 2 — edge case**
- **Given** an order is already picked up,
- **When** I attempt to move it back to preparing,
- **Then** the system rejects the invalid status change.

## US-08 — Customer — Should

As a customer, I want to review my previous orders so that I can remember what I purchased.

**Acceptance criterion 1 — normal case**
- **Given** I have placed previous orders and am viewing my own order history,
- **When** I open order history,
- **Then** I see my previous order numbers, items, and statuses.

**Acceptance criterion 2 — edge case**
- **Given** I have no previous orders,
- **When** I open order history,
- **Then** I see a message explaining that my history is empty.

## US-09 — Café manager — Should

As an authorized café manager, I want to update a menu item's availability so that customers do not order sold-out products.

**Acceptance criterion 1 — normal case**
- **Given** I am an authorized manager and an item is available,
- **When** I mark it sold out,
- **Then** customers can see that it cannot be ordered.

**Acceptance criterion 2 — edge case**
- **Given** I am not an authorized manager,
- **When** I attempt to change item availability,
- **Then** the change is rejected and the menu remains unchanged.

## Copilot INVEST review

**Review prompt:** Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.

**Review results and decisions:** Pending the student's actual Copilot Chat review. Do not invent review feedback.
