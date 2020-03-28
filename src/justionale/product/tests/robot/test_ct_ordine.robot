# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s justionale.product -t test_ordine.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src justionale.product.testing.JUSTIONALE_PRODUCT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/justionale/product/tests/robot/test_ordine.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Ordine
  Given a logged-in site administrator
    and an add Riunione form
   When I type 'My Ordine' into the title field
    and I submit the form
   Then a Ordine with the title 'My Ordine' has been created

Scenario: As a site administrator I can view a Ordine
  Given a logged-in site administrator
    and a Ordine 'My Ordine'
   When I go to the Ordine view
   Then I can see the Ordine title 'My Ordine'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Riunione form
  Go To  ${PLONE_URL}/++add++Riunione

a Ordine 'My Ordine'
  Create content  type=Riunione  id=my-ordine  title=My Ordine

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Ordine view
  Go To  ${PLONE_URL}/my-ordine
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Ordine with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Ordine title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
