describe('Calculator End-to-End Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5000');
  });

  it('loads the calculator page correctly', () => {
    cy.contains('Simple Calculator');
    cy.get('form').should('exist');
  });

  it('should add two numbers', () => {
    cy.get('input[name="num1"]').type('5');
    cy.get('input[name="num2"]').type('3');
    cy.get('select[name="operation"]').select('add');
    cy.get('input[type="submit"]').click();

    // Wait for the page to load and check if the result is displayed correctly
    cy.get('h2', { timeout: 10000 }).should('contain', 'Result: 8');
  });

  it('should subtract two numbers', () => {
    cy.get('input[name="num1"]').type('10');
    cy.get('input[name="num2"]').type('4');
    cy.get('select[name="operation"]').select('subtract');
    cy.get('input[type="submit"]').click();

    // Wait for the page to load and check if the result is displayed correctly
    cy.get('h2', { timeout: 10000 }).should('contain', 'Result: 6');
  });

  it('should handle division by zero', () => {
    cy.get('input[name="num1"]').type('5');
    cy.get('input[name="num2"]').type('0');
    cy.get('select[name="operation"]').select('divide');
    cy.get('input[type="submit"]').click();

    // Wait for the page to fully load and the result to be displayed
    cy.get('h2', { timeout: 10000 }).should('contain', 'Result: Division by zero is not allowed');
  });
});
