import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { AdminRootComponent } from './admin-root/admin-root.component';
import { QuestionDashboardComponent } from './question-bank/question-dashboard/question-dashboard.component';
import { AssessmentDashboardComponent } from './assessment/assessment-dashboard/assessment-dashboard.component';
import { CreateAssessmentComponent } from './assessment/create-assessment/create-assessment.component';
import { CoursesDashboardComponent } from './courses/courses-dashboard/courses-dashboard.component';

const routes: Routes = [
  { path: '', component: AdminRootComponent,
    children: [
      { path: '', component:  DashboardComponent },
      { path: 'reports', component:  DashboardComponent },
      { path: 'question-bank', component: QuestionDashboardComponent},
      { path: 'assessment/list', component: AssessmentDashboardComponent},
      { path: 'assessment/create', component: CreateAssessmentComponent},
      { path: 'courses', component: CoursesDashboardComponent},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
