'use strict';

module.exports = (sequelize, DataTypes) => {
    const employee = sequelize.define('employee', {
        id_employee: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING(30),
        },
        surname: {
            type: DataTypes.STRING(30),
        },
        mail: {
            type: DataTypes.STRING(30),
        },
        password: {
            type: DataTypes.STRING(30),
        },
        is_active: {
            type: DataTypes.BOOLEAN,
            defaultValue: false
        },
        id_center: {
            type: DataTypes.INTEGER
        }
    }, {
        freezeTableName: true,
        timestamps: false,
        underscored: true,
        name: {
            singular: 'employee',
            plural: 'employee'
        }
    });

    employee.associate = models => {
        employee.belongsTo(models.transfusion_center, {
            foreignKey: 'id_center'
        });
    };

    return employee;
};
