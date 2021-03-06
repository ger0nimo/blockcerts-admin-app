describe("Basic UI", () => {
  before(() => {
    // log in only once before any of the tests run.
    cy.login();
  });

  it("Should find form element at /add_credential", () => {
    cy.visit("/add_credential");
    cy.get("form[data-test-id=app-credential-form]").should("exist");
  });

  it("Should find form element at /add_issuance", () => {
    cy.visit("/add_issuance");
    cy.get("form[data-test-id=app-issuance-form]").should("exist");
  });

  it("Should find view title at /manage_credentials", () => {
    cy.visit("/manage_credentials");
    cy.get("h1[data-test-id=app-credential-manage-title]")
      .should("exist")
      .should("contain", "Manage Credentials");
  });
});
