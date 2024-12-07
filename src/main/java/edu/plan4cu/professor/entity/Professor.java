package edu.plan4cu.professor.entity;

import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "Professor")
@Data
@Getter
@Setter
public class Professor {
    @Id
    @Column(name = "p_uni")
    private String id;
    private String firstName;
    private String lastName;
}