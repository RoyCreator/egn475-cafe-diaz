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

As a kitchen staff member, I want to start preparing a received order so that the kitchen can track work in progress.

**Acceptance criterion 1 — normal case**
- **Given** an order is received and I am authorized staff,
- **When** I select Start preparing,
- **Then** its status changes to preparing on the kitchen board.

**Acceptance criterion 2 — edge case**
- **Given** an order is already picked up,
- **When** I attempt to move it back to preparing,
- **Then** the system rejects the invalid status change.

## US-10 — Kitchen staff — Must

As a kitchen staff member, I want to mark a prepared order as ready so that the customer knows it can be picked up.

**Acceptance criterion 1 — normal case**
- **Given** an order is preparing and I am authorized kitchen staff,
- **When** I mark the order ready,
- **Then** the status becomes ready and is visible to the customer.

**Acceptance criterion 2 — edge case**
- **Given** an order is still received and has not started preparation,
- **When** I try to mark it ready,
- **Then** the system rejects the change and keeps its existing status.

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

## Copilot INVEST review and decisions

**First prompt:** "Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only."

**Follow-up prompt:** "Please review the complete USER_STORIES.md file, including US-01 through US-09. US-01 already specifies an empty-menu message, so check that criterion again. Review every story against INVEST. Identify only specific problems, including missing edge cases or stories that should be split. Do not rewrite the stories."

| Copilot flag | Decision | Reason |
| --- | --- | --- |
| US-01 has no empty-menu behavior | Rejected | US-01 already says to display a message when no items are available. |
| US-02 needs empty-submission handling | Rejected as misplaced | US-02 is item selection; US-03 already handles empty submissions. |
| US-03 includes payments and needs splitting | Rejected | US-03 does not process payments; payment is out of scope. |
| US-04 needs sold-out-item handling | Partly accepted, assigned to US-03 | Submission must reject sold-out items, not silently confirm them. |
| US-05 needs pickup-time estimation | Rejected | The story concerns status, not estimated pickup times. |
| US-06 needs failed SMS/email handling | Rejected | The kitchen board does not send notifications. |
| US-07 concerns registration/login | Rejected | US-07 concerns kitchen status changes, not accounts. |
| US-08 needs failed-login handling | Rejected | The story concerns order history, not login. |
| US-09 concerns analytics | Rejected | The story concerns menu availability, not analytics. |

**Additional independent improvement:** Split the original US-07 status progression into smaller stories: US-07 starts preparation and US-10 marks an order ready. Each now describes one distinct staff action and has two testable acceptance criteria.

**Additional acceptance check for US-03 (sold-out item):**
- **Given** my order contains an item that has become sold out,
- **When** I submit the order,
- **Then** the system rejects submission and identifies the unavailable item.

This third check supplements the two required criteria and addresses a useful part of Copilot's US-04 feedback.
