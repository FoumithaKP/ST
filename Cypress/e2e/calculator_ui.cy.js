describe('Calculator UI Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5000');
  });

  it('should display the calculator title', () => {
    cy.contains('Simple Calculator');
  });

  it('should show the result when numbers are added', () => {
    cy.get('input[name="num1"]').type('4');
    cy.get('input[name="num2"]').type('5');
    cy.get('select[name="operation"]').select('add');
    cy.get('input[type="submit"]').click();
    cy.get('h2').should('contain', 'Result: 9');
  });

  it('should show the result when numbers are subtracted', () => {
    cy.get('input[name="num1"]').type('10');
    cy.get('input[name="num2"]').type('4');
    cy.get('select[name="operation"]').select('subtract');
    cy.get('input[type="submit"]').click();
    cy.get('h2').should('contain', 'Result: 6');
  });

  it('should show the result when numbers are multiplied', () => {
    cy.get('input[name="num1"]').type('6');
    cy.get('input[name="num2"]').type('3');
    cy.get('select[name="operation"]').select('multiply');
    cy.get('input[type="submit"]').click();
    cy.get('h2').should('contain', 'Result: 18');
  });

  it('should show the result when divided (and handle division by zero)', () => {
    cy.get('input[name="num1"]').type('10');
    cy.get('input[name="num2"]').type('2');
    cy.get('select[name="operation"]').select('divide');
    cy.get('input[type="submit"]').click();
    cy.get('h2').should('contain', 'Result: 5');

    // Division by zero case
    cy.get('input[name="num1"]').clear().type('10');
    cy.get('input[name="num2"]').clear().type('0');
    cy.get('select[name="operation"]').select('divide');
    cy.get('input[type="submit"]').click();
    cy.get('h2').should('contain', 'Result: Division by zero is not allowed');
  });
});
