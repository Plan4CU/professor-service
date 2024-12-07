package edu.plan4cu.professor.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Entity
@Table(name = "Professor")
@Data
public class Professor {
    @Id
    @Column(name = "p_uni")
    private String id;
    private String firstName;
    private String lastName;
}