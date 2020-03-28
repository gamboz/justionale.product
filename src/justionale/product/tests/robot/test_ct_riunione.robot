# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s justionale.product -t test_riunione.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src justionale.product.testing.JUSTIONALE_PRODUCT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/justionale/product/tests/robot/test_riunione.robot
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

Scenario: As a site administrator I can add a Riunione
  Given a logged-in site administrator
    and an add Riunione form
   When I type 'My Riunione' into the title field
    and I submit the form
   Then a Riunione with the title 'My Riunione' has been created

Scenario: As a site administrator I can view a Riunione
  Given a logged-in site administrator
    and a Riunione 'My Riunione'
   When I go to the Riunione view
   Then I can see the Riunione title 'My Riunione'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Riunione form
  Go To  ${PLONE_URL}/++add++Riunione

a Riunione 'My Riunione'
  Create content  type=Riunione  id=my-riunione  title=My Riunione

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Riunione view
  Go To  ${PLONE_URL}/my-riunione
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Riunione with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Riunione title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
